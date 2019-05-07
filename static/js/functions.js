$(document).ready(function() {

    $('.addIngredient').click(function() {

        var NewIngredient = '<div class="input-field col s12"><input id="ingredients" type="text" name="ingredients"><label for="ingredients">ingredient</label></div>'

        $(".ingredients").append(NewIngredient);
        var NewIngredient = ""
        $('select').material_select();
    });
    
   $("i").click(function() {
  console.log($(this).parent()[0].id);
});

});
