function prepareDocument(){



	$('#submit_review').click(addProductReview);
	$('#review_form').addClass('hide-review');
	$('#add_review').click(slideToggleReviewForm);
	$('#add_review').addClass('visible'); 
	$('#cancel_review').click(slideToggleReviewForm); 



	// toggles visibility of 'write review' link and the review form
	function slideToggleReviewForm(){

		$('#review_form').slideToggle();
		$('#add_review').slideToggle();
	}



	function addProductReview(){
		//build an object of review data to submit
		var review = {
			title: $('#id_title').val(),
			content: $('#id_content').val(),
			rating: $('#id_rating').val(),
			slug: $('#id_slug').val(),
		}
		//make request, process response
		$.post('/review/product/add/', review, 
			function(response){
				$('#review_errors').empty();
				//evaluate the 'success' parameter
				if(response.success == 'True'){
					//disable the submit button 
					$('#submit_review').attr('disabled', 'disabled');
					//id this is the first review, get rid of 'no review' text
					$('#no_reviews').empty();
					//add the new reviews to the reviews section
					$('#reviews').prepend(response.html).slideDown();
					//get the newly added review and style it
					new_review = $('#reviews').children(':first');
					new_review.addClass('new_review');
					//hide teh review form
					$('#review_form').slideToggle();
				}
				else{
					//add the error text to review errors div
					$('#review_errors').append(response.html);
				}
			}, 'json');
	}







}



$(document).ready(prepareDocument)