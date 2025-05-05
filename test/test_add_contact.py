# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.filling_fields(Contact(firstname="ewfweqf", middlename="erferfg", lastname="wfqwvdv",
                    nickname="wfefr", title="wfewqc", company="cwef", address="wfeqrr",
                    phonehome="2343", phonemobile="5432", phonework="34345", phonefax="3453",
                    email="rr@tt.oo", email2="dsfd@err.yy", email3="dvdfwe@tt.yy", homepage="fewfrew",
                    bday="28", bmonth="October", byear="4000", aday="28", amonth="October", ayear="1000"))
    app.session.logaut()
