function Movie(title, rate){
	this.title = title;
	this.rate = rate;
}

var movies = [];
var num_of_movie = 1;
var rate = 0;
var rates = [];
function set_rate(ocena){
	rate = ocena;
}

function check_if_user_exists(login){
	// if(login!=''){
		set_new_user(login.toLowerCase())
	// }else{
		// $('#message').text('Wpisz login by rozpocząć.');
	// }
}
function set_new_user(login){
	$.ajax({
		type: "POST",
		url: "set_login.php",
		data: { q : login },
		async: true,
		}).done(function(data) {
			// if(data == 'true'){
				// alert('Dodano użytkownika');
				set_questions();
			// }else{
				// $('#message').text('Użytkownik o podanej nazwie istnieje. Prosze wpisać inną nazwę.');
			// }
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
	if(num_of_movie > 3){
		alert(rates);
		for(var i = 0; i < movies.length; i++){
			alert(movies[i][1] + " " + rates[i] );
		}
		$('#center').load('allRates.html');	
	}else{
		// if(rate > 0){

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

