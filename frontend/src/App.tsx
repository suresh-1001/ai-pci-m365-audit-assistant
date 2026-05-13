import { Link, Route, Routes } from 'react-router-dom'
import { DashboardPage } from './pages/DashboardPage'
import { LoginPage } from './pages/LoginPage'
import { M365PosturePage } from './pages/M365PosturePage'
import { EvidencePage } from './pages/EvidencePage'
import { AdminPage } from './pages/AdminPage'

export function App() {
  return <div className="min-h-screen bg-slate-100"><nav className="p-4 bg-slate-900 text-white flex gap-4">
    <Link to="/">Dashboard</Link><Link to="/m365">M365 Posture</Link><Link to="/evidence">Evidence</Link><Link to="/admin">Admin</Link><Link to="/login">Login</Link>
  </nav><main className="p-6"><Routes>
    <Route path="/" element={<DashboardPage />} />
    <Route path="/m365" element={<M365PosturePage />} />
    <Route path="/evidence" element={<EvidencePage />} />
    <Route path="/admin" element={<AdminPage />} />
    <Route path="/login" element={<LoginPage />} />
  </Routes></main></div>
}
