$(document).ready(function() {
    
    $('.addIngredient').click(function() {
        var NewIngredient = '<div class="input-field"><input id="ingredients" type="text" name="ingredients"><label for="ingredients">ingredient</label></div>'
        $(".ingredients").append(NewIngredient);
        var NewIngredient = ""
        $('select').material_select();
    });
    
    $('.addStep').click(function() {
        var NewStep = '<li><div class="input-field"><textarea  name="directions" class="materialize-textarea"></textarea><label for="directions"></label></div></li>'
        $(".directions").append(NewStep);
        var NewStep = ""
        $('select').material_select();
    });
});
