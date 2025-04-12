import { Button } from '@/components/ui/button';
import { useFrappeAuth } from 'frappe-react-sdk';
import { Chatbox } from '@/components/chat/Chatbox';

export const Home = () => {
  const { currentUser, logout } = useFrappeAuth();
  console.log(currentUser);
  return (
    <div className='flex flex-col items-center justify-center gap-4 min-w-[80%]'>
      <h1 className='text-[#ee414b] uppercase text-[40px]'>
        welcome to doodlechat
      </h1>
      {currentUser ? (
        <>
          <Button>Hi {currentUser}</Button>
          <Button className='cursor-pointer' onClick={logout}>
            Logout
          </Button>
        </>
      ) : (
        <a href='/login' className='cursor-pointer'>
          <Button className='cursor-pointer'>Go to Login</Button>
        </a>
      )}

      <Chatbox></Chatbox>
    </div>
  );
};
