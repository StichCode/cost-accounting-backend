from src.objects.factory import db


def get_one_by_id(model, _id):
    return model.query.filter_by(id=_id).first()


def get_all(model):
    return model.query.all()


def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()


def delete_instance(model, _id):
    model.query.filter_by(id=_id).delete(synchronize_session=False)
    commit_changes()


def edit_instance(model, _id, kwargs):
    instance = model.query.filter_by(id=_id).all()[0]
    for attr, new_value in kwargs.items():
        setattr(instance, attr, new_value)
    commit_changes()


def commit_changes():
    db.session.commit()