$(document).ready(function(){

	// función básica de manejo de data
	function manageResponse(response, itemToClean, itemsContainer){
		itemToClean.empty();

		itemsContainer.append("<h4> Item Random " + itemsContainer.find("h4").length + "</h4>"+
			"<ul>"+
			"<li>" +response.responseText+ " </li>"+
			"</ul>"
		);
		console.log(response.responseJSON);
	}
	// Creando Fields para el formulario
	$(".add-button").on("click", function(){

		// definimos cantidad de inputs
		var num_inputs = $("#quantity").val();
		
		
		

		// agregamos esos inputs al form
		for( var i = 0; i < num_inputs; i++){
			$("#form-container").append(
				"<div class='label-container'>"+
					"<label>Label-" + i +"</label>"+
				"</div>"+
				"<div class='input-container'>"+
					"<input id='item-" + i +"' class='form-input' type='text'>" +
				"</div>"
			);
		}
	});

	// Recolectando la data para enviar al JSON
	$("#send-data").on("click", function(){
		var data = {};
		var inputs = $(".form-input");

		for (var i = 0; i < inputs.length; i++){
			data["item-"+i] = inputs[i].value;
		}
		$.ajax({
			method: "POST",
			url: "/save",
			data: JSON.stringify(data),
			contentType: "application/json",
			complete: function(resp){
				console.log(resp)
				manageResponse(resp, $("#form-container"),$(".results .row") )

			}
		});
		

	});



});