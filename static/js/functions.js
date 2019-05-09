$(document).ready(function() {

    $('.addIngredient').click(function() {

        var NewIngredient = '<div class="input-field col s12"><input id="ingredients" type="text" name="ingredients"><label for="ingredients">ingredient</label></div>'

        $(".ingredients").append(NewIngredient);
        var NewIngredient = ""
        $('select').material_select();
    });

    $('i').click(function() {
        var id = ($(this).parent()[0].id);
        console.log(id)
        $('input[value=' + id + ']').removeClass('active').addClass('selected');


    });

   
        // Get height for textarea div in edit/add recipe routes
        height = $('.height').outerHeight();
        console.log(height);
        $(".directions").outerHeight(height);



});
