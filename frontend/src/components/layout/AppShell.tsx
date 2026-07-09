import {
  BarChart3,
  Bot,
  CandlestickChart,
  LayoutDashboard,
  Settings,
  Workflow,
} from "lucide-react";
import { NavLink, Outlet } from "react-router-dom";

import { cn } from "@/lib/utils";

const navigation = [
  { to: "/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { to: "/bots", label: "Bots", icon: Bot },
  { to: "/strategies", label: "Strategies", icon: Workflow },
  { to: "/markets", label: "Markets", icon: CandlestickChart },
  { to: "/trades", label: "Trades", icon: CandlestickChart },
  { to: "/analytics", label: "Analytics", icon: BarChart3 },
  { to: "/settings", label: "Settings", icon: Settings },
];

export function AppShell() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <aside className="fixed inset-y-0 w-64 border-r border-border bg-zinc-950 p-5">
        <div className="mb-8 text-lg font-semibold">Trading Platform</div>
        <nav className="space-y-1" aria-label="Primary navigation">
          {navigation.map(({ to, label, icon: Icon }) => (
            <NavLink
              key={to}
              to={to}
              className={({ isActive }) =>
                cn(
                  "flex items-center gap-3 rounded-md px-3 py-2 text-sm text-muted-foreground",
                  "hover:bg-zinc-900 hover:text-foreground",
                  isActive && "bg-zinc-900 text-foreground",
                )
              }
            >
              <Icon className="size-4" aria-hidden="true" />
              {label}
            </NavLink>
          ))}
        </nav>
      </aside>
      <main className="ml-64 min-h-screen p-8">
        <Outlet />
      </main>
    </div>
  );
}
