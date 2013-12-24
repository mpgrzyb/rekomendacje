var movies = [];
var num_of_movie = 1;
var rate = 0;
var rates = [];
var moviesToSend = [];
var userLogin = "";
var userId = 0;

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
function fill_rates(){
	for(var i = 0; i < rates.length; i++){
		movies[i][2] = rates[i];
		movies[i][3] = userId;
	}
	set_rates();
}

function get_next_movie(){
	if(num_of_movie == 20){
		rates.push(rate);
		fill_rates();
	}else{
		photo.src = 'http://filman.pl/' + movies[num_of_movie][2];
		title.innerHTML = movies[num_of_movie][1];
		
		rates.push(rate);

		rate = 0;
		num_of_movie = num_of_movie + 1;	
		$('#message').text('');
		// odznaczenie gwiazdek
		document.getElementById("out").checked = true;
		}
		// else{
			// $('#message').text('Oceń film');
		// }
	}
// }

function set_rates(){
	var tablica = JSON.stringify(movies);
	$.ajax({
		type: "POST",
		url: "set_rates.php",
		data: { q : tablica },
		async: true,
		}).done(function(data) {
			$('#center').html(data);
			
			// if(data == 'true'){
				// alert('Dodano użytkownika');
				// set_questions();
			// }else{
				// $('#message').text('Użytkownik o podanej nazwie istnieje. Prosze wpisać inną nazwę.');
			// }
	});
}