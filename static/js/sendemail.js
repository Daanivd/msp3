function sendMail(contactForm) {
    emailjs.send('default_service', 'template_kM7czE4k', {
            'from_name': contactForm.name.value,
            'from_email': contactForm.email.value,
            'subject': contactForm.subject.value,
            'message': contactForm.message.value
        })
        .then(
            function(response) {
                console.log('SUCCESS', response);
            },
            
            function(error) {
                console.log('FAILED', error);
            }
        );
    return false; // To block from loading a new page
}

