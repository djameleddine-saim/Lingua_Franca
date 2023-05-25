
        document.getElementById('translationForm').addEventListener('submit', function(event) {
            var textInput = document.querySelector('input[name="text"]');
            if (!textInput.value.trim()) {
                event.preventDefault();
                textInput.classList.add('is-invalid');
            }
        });