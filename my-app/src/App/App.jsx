import './App.css';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Root from '../components/Root/Root.jsx';
import Error from '../components/Error.jsx';

// Pages
import { Home } from '../components/Pages/Home/Home.jsx';
import { Movies } from '../components/Pages/Movies/Movies.jsx';
import Users from '../components/Pages/Users/Users.jsx';
import Rents from '../components/Pages/Rents/Rents.jsx';

// Movie CRUD
import CreateMovie from '../components/Pages/Movies/CRUD/Create/CreateMovie.jsx';
import ReadMovies from '../components/Pages/Movies/CRUD/Read/ReadMovies.jsx';
import UpdateMovies from '../components/Pages/Movies/CRUD/Update/Update.jsx';
import DeleteMovies from '../components/Pages/Movies/CRUD/Delete/DeleteMovie.jsx';
import MovieDetail from '../components/Pages/Movies/CRUD/Update/MovieDetail.jsx';

// User CRUD
import CreateUser from '../components/Pages/Users/CRUD/Create/CreateUser.jsx';
import ReadUsers from '../components/Pages/Users/CRUD/Read/ReadUsers.jsx';
import UpdateUsers from '../components/Pages/Users/CRUD/Update/UpdateUser.jsx';
import DeleteUsers from '../components/Pages/Users/CRUD/Delete/DeleteUser.jsx';
import UserDetail from '../components/Pages/Users/CRUD/Update/UserDetail.jsx';

// Rent CRUD
import CreateRent from '../components/Pages/Rents/CRU/Create/CreateRent.jsx';
import ReadRents from '../components/Pages/Rents/CRU/Read/ReadRents.jsx';
import UpdateRents from '../components/Pages/Rents/CRU/Update/UpdateRent.jsx';
import RentDetail from '../components/Pages/Rents/CRU/Update/RentDetail.jsx';

// Home pages
import HomeMovies from '../components/Pages/Movies/HomeMovies.jsx';
import UsersHome from '../components/Pages/Users/UsersHome.jsx';
import RentsHome from '../components/Pages/Rents/RentsHome.jsx';

const router = createBrowserRouter([
  { 
    path: '/', 
    element: <Root />, 
    errorElement: <Error/>,
    children: [
      { path: '/', element: <Home/> },
      { 
        path: 'movies', 
        element: <Movies />,
        children: [
          { path: '', element: <HomeMovies/> },
          { path: 'create', element: <CreateMovie/> },
          { path: 'read', element: <ReadMovies/> },
          { path: ':movieId', element: <MovieDetail/> },
          { path: 'update', element: <UpdateMovies/> },
          { path: 'delete', element: <DeleteMovies/> }
        ]
      },
      { 
        path: 'users', 
        element: <Users />,
        children: [
          { path: '', element: <UsersHome/> },
          { path: 'create', element: <CreateUser/> },
          { path: 'read', element: <ReadUsers/> },
          { path: 'update', element: <UpdateUsers/> },
          { path: 'delete', element: <DeleteUsers/> },
          { path: ':userId', element: <UserDetail/> }
        ]
      },
      { 
        path: 'rents', 
        element: <Rents />,
        children: [
          { path: '', element: <RentsHome/> },
          { path: "create", element: <CreateRent/> },
          { path: "read", element: <ReadRents/> },
          { path: "update", element: <UpdateRents/> },
          { path: ":rentId", element: <RentDetail/> }
        ]
      }
    ]
  }
]);

export default function App() {
  return <RouterProvider router={router}/>
}