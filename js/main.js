var movies = [];
var num_of_movie = 1;
var rate = 0;
var rates = [];
var moviesToSend = [];
var userLogin = "";
var userId = 0;
var recommendations_ready = false;

function set_rate(ocena){
	rate = ocena;
}

function check_if_user_exists(login, password){
	if(login!='' && password!=''){
		set_new_user(login.toLowerCase(), password.toLowerCase())
	}else{
		$('#message').text('Wpisz login by rozpocząć.');
	}
}
function set_new_user(login, password){
	$.ajax({
		type: "POST",
		url: "set_login.php",
		data: { q : login, w : password },
		async: true,
		}).done(function(data) {
			if(data != 'false'){
				userId = data;
				userLogin = login; 
				set_questions();
			}else{
				$('#message').text('Użytkownik o podanej nazwie istnieje, hasło jest niepoprawne. Zmień login by utworzyć nowego użytkownika.');
			}
	});
}
function set_questions () {
	are_recommendations_ready();
	$('#center').load('rate.html');
	get_top_movies();
}
function get_top_movies() {
	$.ajax({
		type: "POST",
		url: "get_top_movies.php",
		data: { q : userId },
		async: true,
		}).done(function(data) {
			var line = data.split(";");
			for(var i = 0; i < line.length; i++){
				var col = line[i].split("+");
				movies.push(col);				
			}
			photo = document.getElementById('poster');
			title = document.getElementById('title');

			photo.src = 'http://filman.pl/' + movies[0][2];
			title.innerHTML = movies[0][1];			
	});	
}

function get_next_movie(){
	if(rate > 0){
			set_movie_rate(movies[num_of_movie-1][0], rate);			
	}else{
		set_movie_rate(movies[num_of_movie-1][0], -1);			
	}
	photo.src = 'http://filman.pl/' + movies[num_of_movie][2];
	title.innerHTML = movies[num_of_movie][1];

	rate = 0;
	num_of_movie = num_of_movie + 1;	
	$('#message').text('');
	// odznaczenie gwiazdek
	document.getElementById("out").checked = true;	
}

function set_movie_rate(movieId, rate){
	$.ajax({
		type: "POST",
		url: "set_rate.php",
		data: { _movieId : movieId, _userId : userId, _rate : rate },
		async: true,
		}).done(function(data) {
			are_recommendations_ready();
			// $('#center').html(data);
			// if(data == 'true'){
				// alert('Dodano użytkownika');
				// set_questions();
			// }else{
				// $('#message').text('Użytkownik o podanej nazwie istnieje. Prosze wpisać inną nazwę.');
			// }
	});
}
function are_recommendations_ready(){
	$.ajax({
		type: "POST",
		url: "recommendations_ready.php",
		data: { _userId : userId},
		async: true,
		}).done(function(data) {
			if(data>20){
				document.getElementById('recomendations').style.visibility = 'visible';
			}
			// $('#center').html(data);
			// if(data == 'true'){
				// alert('Dodano użytkownika');
				// set_questions();
			// }else{
				// $('#message').text('Użytkownik o podanej nazwie istnieje. Prosze wpisać inną nazwę.');
			// }
	});
}

function get_recommendations(){
	$.ajax({
		type: "POST",
		url: "get_recommendations.php",
		data: { _userId : userId},
		async: true,
		}).done(function(data) {
			$('#center').html(data);
			$('#center').css("height", 400);
			// if(data == 'true'){
				// alert('Dodano użytkownika');
				// set_questions();
			// }else{
				// $('#message').text('Użytkownik o podanej nazwie istnieje. Prosze wpisać inną nazwę.');
			// }
	});
}