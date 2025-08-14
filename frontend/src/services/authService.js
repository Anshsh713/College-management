import axios from 'axios';

const API_URL = "http://127.0.0.1:8000/api";

// Always include cookies in requests
axios.defaults.withCredentials = true;

const login = async ({email, password}) => {
  const response = await axios.post(`${API_URL}/login/`, {
    username: email,
    password:password,
  });


  return response.data;
};


const logout = async () => {
  const token = localStorage.getItem("token");
  if (!token) return;

  await axios.post(
    `${API_URL}/logout/`,
    {},
    {
      headers: {
        Authorization: `Token ${token}`,
      },
    }
  );

  localStorage.removeItem("token");
};


const getCurrentUser = async () => {
  try {
    const response = await axios.get(`${API_URL}/current_user/`);
    return response.data;
  } catch (error) {
    console.error("User fetch failed", error);
    return null;
  }
};

const signup = async (username, email, password) => {
  const response = await axios.post(`${API_URL}/signup/`, {
    username,
    email,
    password,
  });

  return response.data;
};


export default {
  login,
  logout,
  getCurrentUser,
  signup,
};
