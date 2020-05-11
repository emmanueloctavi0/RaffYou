
// Yes no modal
$('#yesNoModal').on('show.bs.modal', function (event) {
    const button = $(event.relatedTarget) // Button that triggered the modal
    const link = button.data('to_link') // Extract info from data-* attributes
    document.getElementById('toLink').pathname = link;
});
