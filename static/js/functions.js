$(document).ready(function() {

            var N = (3).toLocaleString(undefined, { minimumIntegerDigits: 2 });

            $('.addIngredient').click(function() {
                        var newIng = 'ingr' + N;
                        var newQuan = 'quan' + N;
                        var newUnit = 'unit' + N;
                        
                        console.log(newIng);

                        var NewIngredient = '<div class="row"><div class="input-field col s4"><input id="'+newIng+'" type="text" class="validate"><label for="'+newIng+'">ingredient</label></div><div class="input-field col s4"><input id="'+newQuan+'" type="text" class="validate"><label for="'+newQuan+'">Quantity</label></div><div class="input-field col s4"><select><option value="" disabled selected>Units</option><option value="'+newUnit+'">Grams</option><option value="'+newUnit+'">Mililiters</option> </select> <label>Grams or Mililiter?</label></div></div>'
                        $(".ingredients").append(NewIngredient);
                        $('select').material_select();
  N++;
  N = (N).toLocaleString(undefined, {minimumIntegerDigits: 2}); 
  
});

});
