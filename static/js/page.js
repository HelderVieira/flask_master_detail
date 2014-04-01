$(document).ready(function () {
    $('#fieldset-add-row').click(function () {
        clone_field_list('tbody tr:last');
    });



     //Remove row
    $("button[data-toggle=fieldset-remove-row]").click(function() {

        $(this).closest("#fieldset-entry").html("")

    }); //End remove row
});

function clone_field_list(selector) {

    var new_element = $(selector).clone(true);
    var elem_id = new_element.find(':input')[0].id;
    var elem_num = parseInt(elem_id.replace(/.*-(\d{1,4})-.*/m, '$1')) + 1;

    new_element.find(':input').each(function() {
        var id = $(this).attr('id').replace('-' + (elem_num - 1) + '-', '-' + elem_num + '-');
        $(this).attr({'name': id, 'id': id}).val('').removeAttr('checked');
    });
    new_element.find('label').each(function() {
        var new_for = $(this).attr('for').replace('-' + (elem_num - 1) + '-', '-' + elem_num + '-');
        $(this).attr('for', new_for);
    });
    $(selector).after(new_element);

}
