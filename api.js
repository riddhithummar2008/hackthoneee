fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      Authorization: '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',
      'HTTP-Referer': 'http://127.0.0.1:5500/h1_firebase.html#', // Optional. Site URL for rankings on openrouter.ai.
      'X-Title': '', // Optional. Site title for rankings on openrouter.ai.
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/gpt-4o',
      messages: [
        {
          role: 'user',
          content: 'What is the meaning of life?',
        },
      ],
    }),
  });
  