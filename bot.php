<?php
// توکن ربات
$botToken = "7757268669:AAF-oMAe7wuoe6R-2uYrT4Zd3v36P9YX-Dg";
$apiUrl = "https://api.telegram.org/bot$botToken/";

// اطلاعات ایمیل و رمز
$email = "example@email.com";
$password = "example_password";

// دریافت آپدیت از تلگرام
$update = file_get_contents("php://input");
$update = json_decode($update, true);

// بررسی نوع آپدیت
if (isset($update['message'])) {
    $chatId = $update['message']['chat']['id'];
    $firstName = $update['message']['chat']['first_name'] ?? "کاربر";

    if ($update['message']['text'] == "/start") {
        $welcomeText = "سلام $firstName عزیز! 🌟\nخوش اومدی! لطفاً روی دکمه زیر کلیک کن تا ایمیل و رمز برات ارسال بشه.";

        $keyboard = [
            "inline_keyboard" => [
                [["text" => "📩 دریافت ایمیل و رمز", "callback_data" => "get_email_password"]]
            ]
        ];

        $replyMarkup = json_encode($keyboard);

        file_get_contents($apiUrl . "sendMessage?chat_id=$chatId&text=" . urlencode($welcomeText) . "&reply_markup=$replyMarkup");
    }
}

// بررسی کلیک روی دکمه
if (isset($update['callback_query'])) {
    $callbackQuery = $update['callback_query'];
    $chatId = $callbackQuery['message']['chat']['id'];
    $callbackData = $callbackQuery['data'];

    if ($callbackData == "get_email_password") {
        $responseText = "📧 **ایمیل:** $email\n🔑 **رمز عبور:** $password\n\nاز این اطلاعات استفاده کن! 😊";

        file_get_contents($apiUrl . "sendMessage?chat_id=$chatId&text=" . urlencode($responseText) . "&parse_mode=Markdown");
    }
}
