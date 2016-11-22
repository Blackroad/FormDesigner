def test_handle_pages(app):
    base_current_page = app.forms.get_number_of_pages()
    app.forms.insert_new_form_page()
    assert app.forms.get_number_of_pages() == base_current_page + 1
    app.forms.delete_form_page()
    assert app.forms.get_number_of_pages() == base_current_page

