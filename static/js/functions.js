$(document).ready(function() {

    $('.addIngredient').click(function() {

        var NewIngredient = '<div class="input-field col s12"><input id="ingredients" type="text" name="ingredients"><label for="ingredients">ingredient</label></div>'

        $(".ingredients").append(NewIngredient);
        var NewIngredient = ""
        $('select').material_select();
    });
    
    
    n=1;
    $('.addStep').click(function() {
        n++;
        var NewStep = '<div class="input-field"><textarea  name="directions" class="materialize-textarea"></textarea><label for="directions">Step '+n+'</label></div>'
        $(".directions").append(NewStep);
        var NewStep = ""
        $('select').material_select();
    });

 
});
