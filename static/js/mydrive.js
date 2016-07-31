$(document).on("click", "#deleteBtn", function () {
     var id = $(this).data('id');
     $(".modal-body #id_file_id").val( id );
     });

$(document).ready(function(){
$('#fileblock').slimScroll({
    position: 'right',
    height: '400px',
    railVisible: true,
    alwaysVisible: false
});
});

$(document).ready(function() {
    $('#fileTable').DataTable({
    responsive:true});
} );