    function add_datetimepicker(inputid) {
	var field = $(inputid);
	field.datetimepicker({
        format: 'DD.MM.YYYY HH:mm:SS',
            language: 'de'
	});
    }

    function add_datepicker(inputid) {
        var field = $(inputid);
        field.datetimepicker({
            format: 'DD.MM.YYYY',
            language: 'de',
	    pickDate: false
        });
    }
