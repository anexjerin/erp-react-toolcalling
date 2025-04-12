import { useForm, SubmitHandler } from 'react-hook-form';
import { Button } from '@/components/ui/button';
import { useFrappeAuth } from 'frappe-react-sdk';
import { useEffect } from 'react';
import { useNavigate } from 'react-router';
import { Chatbox } from '@/components/chat/Chatbox';


import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';

type Inputs = {
  email: string;
  password: string;
};

export function Login() {
  const { login, currentUser } = useFrappeAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (currentUser) {
      navigate('/');
    }
  }, [currentUser, navigate]);

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>();
  const onSubmit: SubmitHandler<Inputs> = (data) => {
    login({ username: data.email, password: data.password });
    console.log(data);
  };

  return (
    <Card className='w-[350px]'>
      <CardHeader>
        <CardTitle>Login</CardTitle>
        <CardDescription>Login using your frappe account</CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit(onSubmit)}>
          <div className='grid w-full items-center gap-4'>
            {/* {currentUser && <Button>Welcome, {currentUser}</Button>} */}
            <div className='flex flex-col space-y-1.5'>
              <Label htmlFor='name'>Name</Label>
              <Input
                id='name'
                placeholder='Enter your email'
                {...register('email', { required: true })}
              />
              {errors.email && (
                <span className='text-red-400'>This field is required</span>
              )}
            </div>
            <div className='flex flex-col space-y-1.5 '>
              <Label htmlFor='password'>Password</Label>
              <Input
                id='password'
                placeholder='Enter your password'
                type='password'
                {...register('password', { required: true })}
              />
              {errors.password && (
                <span className='text-red-400'>This field is required</span>
              )}
            </div>
            <div className='flex flex-col space-y-1.5 '>
              <Button type='submit' className='cursor-pointer'>
                Sign In
              </Button>
            </div>
          </div>
        </form>
      </CardContent>
    </Card>
  );
}
