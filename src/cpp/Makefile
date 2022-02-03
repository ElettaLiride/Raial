.DELETE_ON_ERROR:

ROOTCFLAGS  := $(shell root-config --cflags)
ROOTLDFLAGS := $(shell root-config --ldflags)
ROOTLIBS    := $(shell root-config --libs) -lEG
ROOTGLIBS   := $(shell root-config --glibs)


HIPOCFLAGS  := -I$(HIPO4INC)
HIPOLIBS    := -L$(HIPO4LIB) -lhipo4 

LZ4LIBS     := -L$(LZ4DIR)/lib -llz4
LZ4INCLUDES := -I$(LZ4DIR)/lib

CLAS12ANALIB  := -L$(CLAS12ANAHIPO4)/shlib 

CXX       := g++
CXXFLAGS  += -Wall -fPIC $(ROOTCFLAGS) -std=c++11
LD        := g++
LDFLAGS   := $(ROOTLDFLAGS)

AR	  = ar
ARFLAGS	  = -cvr #create,verbose,quick (don't check for replacement, otherwise use r instead)
EXEDIR = $(RICHGEOAL)/bin

all: $(EXEDIR)/filterHipo $(EXEDIR)/richPlots $(EXEDIR)/richPlots1;

$(EXEDIR)/%: %.o
	$(CXX) -o $@ $< $(ROOTCFLAGS) $(ROOTLDFLAGS) $(HIPOLIBS) $(LZ4LIBS)  $(ROOTLIBS)

%.o: %.cxx
	$(CXX) $(CXXFLAGS) -c -o $@ $< $(ROOTCFLAGS) $(HIPOCFLAGS) $(LZ4INCLUDES) 

clean:
	rm richPlots filterHipo richPlots1
