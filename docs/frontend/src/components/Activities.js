import { BASE_URL } from '../config';

// Add the codespace Django REST API endpoint suffix
const DJANGO_API_SUFFIX = '/api';

fetch(`${BASE_URL}${DJANGO_API_SUFFIX}/activities/`);