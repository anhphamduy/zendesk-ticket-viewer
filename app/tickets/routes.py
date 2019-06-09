import math

from flask import abort, current_app, render_template, request, url_for
from zenpy.lib.exception import APIException

from app.tickets import bp


@bp.route('/tickets')
@bp.route('/')
def tickets():
    try:
        tickets = current_app.zenpy.tickets()
        if not tickets:
            return render_template('/tickets/tickets.html', no_tickets=True)
    except APIException:
        abort(503)

    tickets_per_page = current_app.config['TICKETS_PER_PAGE']
    pagination_size = current_app.config['PAGINATION_SIZE']
    total_pages = math.ceil(len(tickets) / tickets_per_page)

    # restrict the bound of the page to min and max page
    page = min(max(request.args.get('page', 1, type=int), 1), total_pages)
    # get tickets of the current pagination page
    try:
        tickets = tickets[(page - 1) *
                          tickets_per_page:page * tickets_per_page]
    except StopIteration:
        # the last page
        tickets = tickets[(page - 1) * tickets_per_page:len(tickets)]

    # get the min and max page in the current pagination state
    min_pagination = max(1, page - pagination_size)
    max_pagination = min(page + pagination_size, total_pages)

    # get all the urls for the pagination bar
    pages = [dict(url=url_for('tickets.tickets', page=i) if i != page else None, display_value=i)
             for i in range(min_pagination, max_pagination + 1)]
    next_url = url_for('tickets.tickets', page=page + 1) \
        if page < total_pages else None
    prev_url = url_for('tickets.tickets', page=page - 1) \
        if page > 1 else None

    context = {
        'tickets': tickets,
        'pages': pages,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render_template('/tickets/tickets.html', **context)


@bp.route('/tickets/<ticket_id>')
def ticket(ticket_id):
    try:
        ticket = current_app.zenpy.tickets(id=ticket_id)
    except APIException:
        abort(503)

    return render_template('/tickets/ticket.html', ticket=ticket)
