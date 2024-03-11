#include <iostream>
#include <random>

int random_generator(){
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(0, 1);

    return dis(gen);
}

void random_sequence(const size_t& num_bits){
    for(size_t i = 0; i < num_bits; i++){
        std::cout<<random_generator();
    }
    std::cout<<std::endl;
}

int main() {
    const size_t NUMBER_BITS = 128;
    random_sequence(NUMBER_BITS);
    return 0;
}