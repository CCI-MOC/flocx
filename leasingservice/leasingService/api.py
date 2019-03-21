from leasingService.flaskapp import app
from flask import render_template, flash, redirect, request
from leasingService.forms import BiddingForm

@app.route('/')
def base():
    return render_template('base.html') 

@app.route('/index')
def index():
    return render_template('index.html', title='FLOCX Leasing Service', page='Home' )


@app.route('/bid/create', methods=['GET', 'POST'])
def bid_create():
    form = BiddingForm()
    #form = BiddingForm(request.form)
    #print(form.errors)
    if request.method == 'POST':
    #if form.validate_on_submit():
        flash('Bid created successfully. Your bid id is a1b2c3d4.')
        return redirect('/index')
    return render_template('bid_create.html', title="Create new Bid", form=form)


@app.route('/bid/accept')
def accept_bid(bid):
    """ Takes in a dictionary object as a bid. Verifies if keys:value pairs confirm
    Returns ok if found acceptable.
    TODO: Create a class called bid and put all related operations in it.
    """
    bid_keys = ['buying_price_hourly',
                'duration_hours',
                'server_config',
                'server_id',
                'server_qty'
                ]
    if all(key in bid for key in bid_keys):
        return 201903210055_01
    else:
        return {'status': 403}


@app.route('/bid/get')
def get_bid(bid_id):
    """Given a bid_id, bidder who owns the bid should be able to see the details of the bid."""

    stored_bid = { 'bid_id':201903210055_01,
                   'buying_price_hourly': 10,
                  'duration_hours': 40,
                  'server_config': {'CPU': 16, 'RAM_GB': 64},
                  'server_id': 'alphnumericid_012',
                  'server_qty': 12
                  }
    if stored_bid['bid_id'] == bid_id:
        return stored_bid
    else:
        return {'status':404}

