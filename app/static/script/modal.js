$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    // $('#distribution-modal').on('show.bs.modal', function (event) {
    //     const button = $(event.relatedTarget) // Button that triggered the modal
    //     const cityId = button.data('source') // Extract info from data-* attributes
    //     const date = button.data('content') // Extract info from data-* attributes
    //     const type_param = button.data('content2') // Extract info from data-* attributes
    //     console.log("hi test")
    //     const modal = $(this)
    //     if (cityId === 'New Distribution') {
    //         modal.find('.modal-title').text(cityId)
    //         $('#distribution-form-display').removeAttr('cityId')
    //     } else {
    //         modal.find('.modal-title').text('Edit Distribution ' + cityId)
    //         $('#distribution-form-display').attr('cityId', cityId)
    //     }

    //     if (date) {
    //         modal.find('.form-control').val(date);
    //     } else {
    //         modal.find('.form-control').val('');
    //     }
   // })


    $('#submit-distribution').click(function () {
        const cID = $('#distribution-modal').find('.form-control1').val()
        const date = $('#distribution-modal').find('.form-control2').val()
        const num_delivered = $('#distribution-modal').find('.form-control3').val()
        const type_param= $('#distribution-modal').find('.form-control4').val()
        // console.log(cID)
        // console.log(date)
        // console.log(num_delivered)
        // console.log(type_param)
        console.log('/create/' + cID + '/' + encodeURIComponent(date) + '/' + num_delivered + '/' + encodeURIComponent(type_param))
        $.ajax({
            type: 'POST',
            url: '/create/' + cID + '/' + encodeURIComponent(date) + '/' + num_delivered + '/' + encodeURIComponent(type_param),
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                // console.log(cId);
                // console.log(date);
                // console.log(numDelivered);
                // console.log(type_param);
                console.log(res.response)
                location.reload();
                
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + encodeURIComponent(remove.data('source')) + '/' + remove.data('content') + '/' + remove.data('content2') ,
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.edit').click(function () {
  
        const state = $(this)
        const cID = state.data('source')
        const date = state.data('content')
        const type_param = state.data('content2')

        $('#edit').click(function () {
            const numDelivered = $('#distribution-modal2').find('.form-control3').val()

            $.ajax({
                type: 'POST',
                url: '/edit/' + cID + '/' + encodeURIComponent(date) + '/'+ encodeURIComponent(type_param),
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify({
                    'num_delivered': numDelivered
                }),
                success: function (res) {
                    console.log(res)
                    location.reload();
                },
                error: function () {
                    console.log('Error');
                }
            });
        });
    });

    $('#search').click(function () {
        const cID = $('#distribution-modal3').find('.form-control1').val()
        const date = $('#distribution-modal3').find('.form-control2').val()
        const type_param = $('#distribution-modal3').find('.form-control3').val()

        $.ajax({
            type: 'POST',
            url: '/search/' + cID + '/' + encodeURIComponent(date)+ '/' + encodeURIComponent(type_param),
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.all').click(function () {
        $.ajax({
            type: 'GET',
            url: '/' ,
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.query').click(function () {
        $.ajax({
            type: 'POST',
            url: '/query' ,
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});