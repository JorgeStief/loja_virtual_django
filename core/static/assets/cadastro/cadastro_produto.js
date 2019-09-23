$.validator.addMethod('require-one', function(value, element){
	return $('input[id="tamanho"]:checked').length>0;
}, "Escolha ao menos um tamanho!");

$(document).ready(function(){
    
    $('#preco').mask('000.000.000.000.000,00', {reverse: true});

    

    var checkboxes = $('.require-one');
    
	var checkbox_names = $.map(checkboxes, function(e, i) {
		return $(e).attr("name")
    }).join(" ");
   
    

    $("#form").validate({
        debug: false,
        groups: {
			checks: checkbox_names
		},
        rules: {
            
            

            cate:{
                required: true,
                

            },
            nome:{
                required: true,
                

            },
            preco:{
                required: true,
                

            },
            descricao: {
                required: true,
            },
            disponivel: {
                required: true,
            },
            imgProd: {
                required: true,
            },
           
        },
        errorPlacement: function (error, element) {
            //alert(element);
            console.log(element);
            error.insertAfter(element).addClass("invalid-feedback")
                 
        },
        messages: {
            cate:{
                required: "Campo Obrigatório"
            },
            nome:{
                required: "Campo Obrigatório"
            },
            preco:{
                required: "Campo Obrigatório"
            },
            descricao:{
                required: "Campo Obrigatório"
            },
            disponivel:{
                required: "Campo Obrigatório"
            },
            imgProd:{
                required: "Campo Obrigatório"
            },
            
        }
    });
    
  });