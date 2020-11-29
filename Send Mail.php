<?php

	function check_mail($mail_id)
	{
		$mail_id filter_var($mail_id , FILTER_SANITIZE_EMAIL);
		if(filter_var($mail_id , FILTER_VALIDATE_MAIL))
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	$to_mail = '';
	$subject = 'Alert';
	$message = '@@@@@';
	$headers = 'From: NoReply';

	$secure_check = check_mail($to_mail);
	if($secure_check == true)
	{
		mail($to_email , $subject , $message , $headers);
	}

?>
