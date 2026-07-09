import { Navigate, Route, Routes } from "react-router-dom";

import { AppShell } from "@/components/layout/AppShell";
import { PlaceholderPage } from "@/pages/PlaceholderPage";

const pages = [
  ["dashboard", "Dashboard"],
  ["bots", "Bots"],
  ["strategies", "Strategies"],
  ["markets", "Markets"],
  ["trades", "Trades"],
  ["analytics", "Analytics"],
  ["settings", "Settings"],
] as const;

export function App() {
  return (
    <Routes>
      <Route path="/login" element={<PlaceholderPage title="Login" />} />
      <Route element={<AppShell />}>
        {pages.map(([path, title]) => (
          <Route
            key={path}
            path={`/${path}`}
            element={<PlaceholderPage title={title} />}
          />
        ))}
      </Route>
      <Route path="*" element={<Navigate to="/dashboard" replace />} />
    </Routes>
  );
}
