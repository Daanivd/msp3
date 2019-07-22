function sendMail(contactForm) {
        emailjs.send("gmail", "template_kM7czE4k", 
            {"from_name":contactForm.name.value,
             "from_email":contactForm.email.value,
             "subject":contactForm.subject.value,
             "message":contactForm.message.value})
        .then(
            function(response) {
                alert("E-mail sent, thank you!");
            },
            function(error) {
                alert("Our apologies, something went wrong./nPlease try again later");
            }
        )
    return false // To block from loading a new page
}