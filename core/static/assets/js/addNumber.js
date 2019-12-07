$(function(){
	$('.addNumber').each(function(i){
		var name = $(this).attr('name');
		var id  = $(this).attr('id');
		if($(this).attr('value') == ""){
			var value = 0
		}
		else{
			var value = $(this).attr('value');
		}
		
		var novoHTML = '<div class="addNumber">'+
							'<form name="" method="get" action="/carrinho/modifica" novalidate>'+
								'<input type="text" name="'+name+' " id="'+id+'" value="'+value+'" class="input'+i+'" />'+
								'<a class="add" onclick="addNumber(\'add\',$(\'.input'+i+'\'))">+</a>'+
								'<a class="remove" onclick="addNumber(\'remove\',$(\'.input'+i+'\'))">-</a>'+
					   		'</form>'+
					   '</div>';
		$(this).parent().append(novoHTML);
		$(this).remove();	
	});
});

function addNumber(tipo, classe){
	var valorAtual = Number(classe.val());
	if(valorAtual<1){
		classe.val('1');
		return false;
	}
	if(tipo=='add'){
		var correcao = valorAtual+1;
		classe.val(correcao);
	}else if(tipo=='remove'){
		var correcao = valorAtual-1;
		
		if(correcao<1){
			classe.val('1');
			return false;
		}else {
			classe.val(correcao);
		}
	}
	//lista_de_ids = {{lista_de_ids}}
	//console.log("entrou")
	let form = $(classe).parent()
	let td_atual = $(form).attr("id")
	//console.log(form)
	let tr = $(form).parent().parent().parent()
	let td = tr.children("td")[0]
    let ind = $(tr).index()
    let id = $(td).html()
    $(form).append("<input type='hidden' name='pro_id' value='" + id + "'>")
	let url = $(form).attr('action')
	let formData = $(form).serializeArray()
	
   //console.log(formData)
    //console.log(lista_de_ids)
	$.ajax({
        type:'GET',
        url:url,
        data:formData,
        dataType:'json',

        success: function(data){
            $(classe).parent().parent().parent().parent().children("td.sub_total").text(data.sub_total)
			$("#total").text(data.total)
			   
        },
        error: function(){
          // alert('Deu Erro');
          console.log('Deu Erro');
        },
         
	});
}
