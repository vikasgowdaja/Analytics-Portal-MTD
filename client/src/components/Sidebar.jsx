import { Link, useLocation, useNavigate } from "react-router-dom";
import { Home, LayoutDashboard, Users, Upload, LogOut,Trash2 } from "lucide-react";
import { supabase } from "@/integrations/supabase/client";

const Sidebar = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const menuItems = [
    { path: "/", label: "Home", icon: <Home size={18} /> },
    { path: "/overview", label: "Overview", icon: <LayoutDashboard size={18} /> },
    { path: "/department", label: "Department", icon: <Users size={18} /> },
    { path: "/upload", label: "Upload", icon: <Upload size={18} /> },
    { path: "/unload", label: "Unload PDFs", icon: <Trash2 size={18} /> },
  ];

  const handleLogout = async () => {
    await supabase.auth.signOut();
    navigate("/auth");
  };

  return (
    <div className="h-screen w-64 bg-gray-900 text-gray-100 flex flex-col p-4">
      {/* Header */}
      <h1 className="text-xl font-bold mb-6 text-center">📊 Analytics Portal</h1>

      {/* Navigation */}
      <nav>
        <ul className="space-y-2">
          {menuItems.map((item) => {
            const isActive = location.pathname === item.path;
            return (
              <li key={item.path}>
                <Link
                  to={item.path}
                  className={`flex items-center gap-3 p-2 rounded-md transition-colors ${
                    isActive
                      ? "bg-gray-800 text-blue-400 font-semibold border-l-4 border-blue-500"
                      : "hover:bg-gray-800 hover:text-blue-300"
                  }`}
                >
                  {item.icon}
                  <span>{item.label}</span>
                </Link>
              </li>
            );
          })}
        </ul>

        {/* Logout placed right below the last menu item */}
        <button
          onClick={handleLogout}
          className="flex items-center gap-3 p-2 rounded-md text-red-400 hover:bg-gray-800 hover:text-red-500 transition-colors mt-4 w-full"
        >
          <LogOut size={18} />
          <span>Logout</span>
        </button>
      </nav>

      {/* Footer */}
      <footer className="text-xs text-center text-gray-500 mt-auto">
        © {new Date().getFullYear()} Analytics System
      </footer>
    </div>
  );
};

export default Sidebar;
