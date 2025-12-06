import React from 'react';

interface HeaderProps {
  title?: string;
  subtitle?: string;
}

const Header: React.FC<HeaderProps> = ({ 
  title = 'Command Center', 
  subtitle = 'Chat with your autonomous advertising agent' 
}) => {
  return (
    <div className="border-b border-slate-200 bg-white">
      <div className="max-w-7xl mx-auto px-6 py-6">
        <h2 className="text-2xl font-semibold text-slate-800">{title}</h2>
        <p className="text-sm text-slate-500 mt-1">{subtitle}</p>
      </div>
    </div>
  );
};

export default Header;