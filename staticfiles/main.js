$(document).ready(function() {
	//Only needed for the filename of export files.
	//Normally set in the title tag of your page.
	document.title='DataTable Excel';
	// DataTable initialisation
	$('#example').DataTable(
		{
			"dom": '<"dt-buttons"Bf><"clear">lirtp',
			"paging": true,
			"autoWidth": true,
			"buttons": [
					{
            extend: 'excelHtml5',
            text: 'Excel',
            customize: function( xlsx ) {
              var source = xlsx.xl['workbook.xml'].getElementsByTagName('sheet')[0];
              source.setAttribute('name','New Name');
						}
					}
			]
		}
	);
});