import { Outlet } from "react-router-dom";
import Navigation from './Navigation/Navigation.jsx';

export default function Root() {
  return (
    <div>
      <Navigation />
      <main>
        <Outlet />
      </main>
    </div>
  );
}
