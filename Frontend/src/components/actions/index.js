

const AUTHENTICATE = "AUTHENTICATE"

export function authenticate(payload) {
    return {
        type: AUTHENTICATE,
        payload: { 
            is_authenticated: true
        }
    }
};