from flask import Blueprint, jsonify, request, json, render_template, redirect
from datetime import datetime
from agriculture.models import *
import os
from flask import flash, request, redirect, url_for
from agriculture.forms import SeedForm, EventForm, PlantForm

main = Blueprint('main', __name__)


#########################    ГЛАВНАЯ   #############################
@main.route('/')
def index():
    managers = User.query.all()
    return render_template('index.html', managers=managers)


#########################    ГЛАВНАЯ   #############################
@main.route('/seed', methods=['GET', 'POST'])
def seed():
    managers = User.query.all()
    form = SeedForm(request.form, obj=Seed())
    if request.method == 'POST':
        seeds = Seed()
        form.populate_obj(seeds)
        db.session.add(seeds)
        db.session.commit()
    if request.args.get('add'):
        pass

    seeds = Seed.query.order_by(Seed.name).all()
    return render_template('seed.html', form=form, seeds=seeds, managers=managers)


@main.route('/plant', methods=['GET', 'POST'])
def plant():
    managers = User.query.all()
    form = SeedForm(request.form, obj=Seed())
    if request.method == 'POST':
        seeds = Seed()
        form.populate_obj(seeds)
        db.session.add(seeds)
        db.session.commit()
    if request.args.get('add'):
        pass

    seeds = Seed.query.order_by(Seed.name).all()
    return render_template('plant.html', form=form, seeds=seeds, managers=managers)


@main.route('/protectionplants', methods=['GET', 'POST'])
def protectionplants():
    managers = User.query.all()
    form = PlantForm(request.form, obj=Plant())
    form.protectionplants_id.choices = [(i.id, i.name) for i in ProtectionPlants.query.order_by(ProtectionPlants.name).all()]
    if request.method == 'POST':
        seeds = Plant()
        form.populate_obj(seeds)
        db.session.add(seeds)
        db.session.commit()
    if request.args.get('add'):
        pass
        Company.users.any(id=user_id)
    category = ProtectionPlants.query.order_by(ProtectionPlants.name).all()
    seeds = Plant.query.join(ProtectionPlants).order_by(ProtectionPlants.name).all()
    return render_template('plant.html', form=form, seeds=seeds, managers=managers, category=category)


#########################    ГЛАВНАЯ   #############################
@main.route('/event', methods=['GET', 'POST'])
def event():
    date = datetime.now()
    managers = User.query.all()
    form = EventForm(request.form, obj=Event())
    events = Event.query.order_by(Event.date.desc()).all()
    form.company_id.choices = [(i.id, i.name) for i in Company.query.order_by().all()]
    form.user_id.choices = [(i.id, f'{i.last_name} {i.first_name}') for i in User.query.order_by(User.last_name).all()]
    if request.args.get('edit'):
        event = Event.query.get(request.args.get('edit'))
        form = EventForm(request.form, obj=event)
        form.company_id.choices = [(i.id, i.name_company) for i in Company.query.order_by().all()]
        form.user_id.choices = [(i.id, f'{i.last_name} {i.first_name}') for i in
                                User.query.order_by(User.last_name).all()]

        if request.method == 'POST':
            form.populate_obj(event)
            db.session.commit()
        return render_template('event.html', form=form, events=events, managers=managers, date=date)

    if request.method == 'POST':
        event = Event()
        form.populate_obj(event)
        db.session.add(event)
        db.session.commit()

    return render_template('event.html', form=form, events=events, managers=managers, date=date)


@main.route('/event_delete/<int:id>', methods=['GET', 'POST'])
def event_delete(id):
    event = Event.query.get(id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('main.event'))


@main.route('/manager/<int:id>', methods=['GET', 'POST'])
def manager(id):
    managers = User.query.all()
    manager = User.query.get(id)
    if request.args.get('company'):
        return render_template('manager_view.html', manager=manager, managers=managers)
    return render_template('manager.html', manager=manager, managers=managers)


@main.route('/manager/view/<int:id>', methods=['GET', 'POST'])
def manager_view(id):
    managers = User.query.all()
    manager = User.query.get_or_404(id)
    return render_template('manager_view.html', manager=manager, managers=managers)


@main.route('/get_calendar', methods=['POST'])
def get_calendar():
    events = Event.query.all()
    list_json = []
    for event in events:
        list_json.append({"date": event.date.strftime("%Y-%m-%d ") + event.time.strftime("%H:%M:%S"),
                          "title": f'{event.company.name_company}-{event.users.last_name}',
                          "description": event.company.name,
                          "url": url_for("main.event", id=event.id)})

    return json.dumps(list_json)


@main.route('/company')
def company():
    managers = User.query.all()
    company = Company.query.all()
    return render_template('company.html', company=company, managers=managers)


@main.route('/api/company_choices', methods=('GET', 'POST'))
def api_arena_choices():
    user_id = request.form['user_id']
    item_list = Company.query.filter(Company.users.any(id=user_id)).all()

    result_list = dict()
    for item in item_list:
        result_list[item.id] = item.name
    return json.dumps(result_list)


@main.route('/api/manager/<int:id>', methods=('GET', 'POST'))
def manager_calendar(id):
    events = Event.query.filter(Event.user_id == id).all()
    list_json = []
    for event in events:
        list_json.append({"date": event.date.strftime("%Y-%m-%d ") + event.time.strftime("%H:%M:%S"),
                          "title": event.company.name_company,
                          "description": event.company.name,
                          "url": url_for("main.event", id=event.id)})

    return json.dumps(list_json)
