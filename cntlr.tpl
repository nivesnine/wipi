<head>
	<title> CntlR </title>
	<script type='text/javascript' src='/static/j.js'></script>
	<link rel="stylesheet" type="text/css" href="/static/foundation.css">
        <meta charset="utf-8"> 
        <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
        <meta name="viewport" content="width=device-width,initial-scale=1"> 
</head>

<body>
	<div class='row'>
		<div class='small-12 columns'>
			<h1>CntlR</h1>
		</div>
		<div class='small-12 columns text-center'>
			<button class='button info' id='up'>UP &#8679;</button>
		</div>
		<div class='small-6 columns text-center'>
			<button class='button info' id='left'>LEFT &#8678;</button>
		</div>
		<div class='small-6 columns text-center'>
			<button class='button info' id='right'>RIGHT &#8680;</button>
		</div>
		<div class='small-12 columns text-center'>
			<button class='button info' id='down'>DOWN &#8681;</button>
		</div>
		<div class='small-12 columns text-center'>
			<button class='button alert' id='stop'>Stop</button>
		<div>
	</div>
</body>

<script>
	var up = 0;
	var left = 0;
	var right = 0;
	var down = 0;

	$('#stop').click(function(){
		$.ajax({
			type: "GET",
			url : "/stop"
		});
		up = 0;
		left = 0;
		right = 0;
		down = 0;
	});

	$('#up').click(function(){
			if(up == 0){
				$.ajax({
					type: "GET",
					url : "/up/on"
				});
				up = 1;
			}
			else{
				$.ajax({
					type: "GET",
					url : "/up/off"
				});
				up = 0;
			}
	});

        $('#left').click(function(){
	                if(left == 0){
                        	$.ajax({
                        	        type: "GET",
                        	        url : "/left/on"
                        	});
                        	left = 1;
                	}
               		else{
                        	$.ajax({
                        	        type: "GET",
                        	        url : "/left/off"
                        	});
                        	left = 0;
                	}
        });

        $('#right').click(function(){
	                if(right == 0){
        	                $.ajax({
        	                        type: "GET",
        	                        url : "/right/on"
        	                });
        	                right = 1;
        	        }
                	else{
                	        $.ajax({
                	                type: "GET",
                	                url : "/right/off"
                	        });
                	        right = 0;
                	}
        });

        $('#down').click(function(){
	                if(down == 0){
	                        $.ajax({
	                                type: "GET",
	                                url : "/down/on"
	                        });
	                        down = 1;
	                }
	                else{
	                        $.ajax({
	                                type: "GET",
	                                url : "/down/off"
	                        });
	                        down = 0;
	                }
        });

</script>

