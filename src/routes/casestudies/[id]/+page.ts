import { error } from '@sveltejs/kit';
import casestudies from '$lib/data/casestudies.json';

export function load({ params }: any) {
    const casestudy = casestudies.find((cs: any) => cs.id === params.id);
    
    if (!casestudy) {
        throw error(404, 'Case study not found');
    }
    
    return {
        casestudy
    };
}
