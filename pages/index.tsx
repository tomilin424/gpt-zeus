import { useEffect, useState } from 'react';

interface Chat {
  id: number;
  model: string;
  timestamp: string;
  preview: string;
}

export default function Home() {
  const [chats, setChats] = useState<Chat[]>([]);
  const [isWebAppReady, setIsWebAppReady] = useState(false);

  useEffect(() => {
    // Инициализация Telegram Web App
    if (window.Telegram?.WebApp) {
      window.Telegram.WebApp.ready();
      window.Telegram.WebApp.expand();
      setIsWebAppReady(true);
    }
  }, []);

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      {/* Header */}
      <header className="flex justify-between items-center p-4 bg-white border-b">
        <button className="p-2">
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
        <div className="text-lg font-semibold">Neurs.AI - ChatGPT 4</div>
        <button className="p-2">
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
        </button>
      </header>

      {/* Voice Assistant Button */}
      <div className="p-4">
        <button className="w-full py-3 px-4 bg-blue-500 text-white rounded-lg flex items-center justify-center space-x-2">
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" />
          </svg>
          <span>Голосовой ассистент</span>
          <span className="ml-2">✨</span>
        </button>
      </div>

      {/* Chat List */}
      <div className="flex-1 overflow-y-auto">
        {chats.map((chat) => (
          <div key={chat.id} className="p-4 border-b bg-white">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center">
                <svg className="w-6 h-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
              </div>
              <div className="flex-1">
                <div className="flex justify-between items-center">
                  <div className="font-medium">{chat.model}</div>
                  <div className="text-sm text-gray-500">{chat.timestamp}</div>
                </div>
                <div className="text-sm text-gray-600 mt-1">{chat.preview}</div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* New Chat Button */}
      <div className="p-4 border-t bg-white">
        <button className="w-full py-3 bg-blue-500 text-white rounded-lg">
          Новый чат
        </button>
      </div>
    </div>
  );
} 