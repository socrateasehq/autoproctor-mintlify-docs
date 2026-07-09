#!/bin/bash
# Download Socratease images from Crisp CDN to local images directory

mkdir -p images/socratease

echo "Downloading question type images..."

# Question Types images
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/mcq_19vhzxl.png" -o images/socratease/mcq.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/mca_1hamxqb.png" -o images/socratease/mca.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/short-text_1mmfrpx.png" -o images/socratease/short-text.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/single-line_7vumvv.png" -o images/socratease/single-line-input.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/code-editor_15uwy03.png" -o images/socratease/coding-editor.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/image_1ptr2gn.png" -o images/socratease/cloze.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/image_uhmcye.png" -o images/socratease/match.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/image_1ylx5tu.png" -o images/socratease/categorize.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/image_1k07j57.png" -o images/socratease/comprehension.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/image_i4j6bl.png" -o images/socratease/document.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/image_14c4uob.png" -o images/socratease/answer-any.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/image_1xp0592.png" -o images/socratease/voice-input.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/image_87z2ih.png" -o images/socratease/autograded-text.png

echo "Downloading results and settings images..."

# Showing Results images
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/release-1_1emq4l8.png" -o images/socratease/result-release-options.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/-/2/a/b/c/2abc2e1da180f600/image_roi4m.png" -o images/socratease/hide-questions-option.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/settings-1_1pd795u.png" -o images/socratease/quiz-settings.png

echo "Downloading question bank images..."

# Question Banks images
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/image_llwwl6.png" -o images/socratease/question-bank-overview.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/image_1jw4g6c.png" -o images/socratease/question-bank-example.png
curl -sL "https://storage.crisp.chat/users/helpdesk/website/2abc2e1da180f600/image_1maxh1.png" -o images/socratease/question-bank-quiz-config.png

echo "Downloading display mode image..."

# Question Display Mode image
curl -sL "https://storage.crisp.chat/users/helpdesk/website/-/2/a/b/c/2abc2e1da180f600/image_1gc30dn.png" -o images/socratease/question-display-mode.png

echo "Done! Downloaded $(ls images/socratease/*.png | wc -l) images."
