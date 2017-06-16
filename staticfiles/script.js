 

function prepareDocument(){




	//loadig box         //not working
	function statusBox(){
		$('<div id="loading">Loading...</div>').prependTo("#main").ajaxStart(function(){

			$(this).show();

		}).ajaxStop(function(){

			$(this).hide();
	})
} 
	



	//tagging functionality to prepareDocument()
	$('#add_tag').click(addTag);

	$('#id_tag').keypress(function(event){ 
		if (event.which == 13 && $('#id_tag').val().length > 2){  
			addTag();
			event.preventDefault();
		}
	});




	function addTag(){
		tag = { tag: $('#id_tag').val(),
				slug: $('#id_slug').val(),
			  };
		$.post('/tag/product/add/', tag, 
			function(response){
				if(response.success == 'True'){
					$('#tags').empty();
					$('#tags').append(response.html);
					$('#id_tag').val('');
				}
			}, 'json');
	}




















	


	

statusBox();
}



$(document).ready(prepareDocument)