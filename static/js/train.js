
$('#train').click(function () {
    $(this).prop("disabled", true);
    $('#loader').addClass('loader');
    $.ajax({
        type: "GET",
        url: "/sendtrain/"
        , success: function (data) {
            $('#duration').html(data.duration);
            $('#loader').removeClass('loader');
            $('#train').prop("disabled", false);
            $('.alert.alert-dismissable.alert-success').show(200);
        }
    });
});
