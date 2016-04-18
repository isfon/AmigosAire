tinymce.init({
	language : 'es',
	theme: "modern",
    selector: "textarea",
    plugins: [
         "advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker",
         "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
         "save table contextmenu directionality emoticons template paste textcolor"
   ],
   toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | l      ink image | print preview media fullpage | forecolor backcolor emoticons",
    file_browser_callback: function(field_name, url, type, win) {
        var url = "http://localhost:8000/admin/filebrowser/browse/?pop=2&type=" + type;

        tinymce.activeEditor.windowManager.open(
            {
                'url': url,
                'width': 820,
                'height': 500,
//                'resizable': "yes",
//                'scrollbars': "yes",
//                'inline': "no",
//                'close_previous': "no"
            },
            {
                'window': win,
                'input': field_name,
//                'editor_id': tinyMCE.selectedInstance.editorId
            }
        );
    }
});