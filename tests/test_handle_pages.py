def test_handle_pages(app):
    app.forms.select_last_page()
    app.forms.insert_new_form_page()
    app.forms.delete_form_page()