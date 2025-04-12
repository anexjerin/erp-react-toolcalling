import React, { ReactNode } from 'react';
import { Navigate } from 'react-router';
import { useFrappeAuth } from 'frappe-react-sdk';

interface ProtectedRouteProps {
  children: ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const { currentUser, isLoading } = useFrappeAuth();

  if (isLoading) {
    return <div>Loading...</div>; // Show a loading state while checking authentication
  } else if (!currentUser) {
    return <Navigate to='/login' replace />;
  }
  return <>{children}</>;
};

export default ProtectedRoute;
